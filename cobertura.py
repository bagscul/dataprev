#!/usr/bin/env python3
"""cobertura.py — cruza os subtopicos da apostila com o banco de questoes.

Para cada capitulo de conteudo da apostila (apostila/capitulos/*.tex), extrai
os subtopicos (subsecao quando o capitulo tem subsecoes; senao, secao) e conta
quantas questoes de banco.json + banco-provas.json tocam cada subtopico, por
correspondencia de palavra-chave no texto da questao (enunciado + alternativas
+ explicacao). Reporta:

  * subtopicos com POUCA/NENHUMA questao (o alvo do relatorio);
  * o gap de granularidade de TAG: quantas questoes casam por palavra-chave em
    QUALQUER tag vs. dentro da(s) tag(s) do bloco (revela subtopico coberto no
    conteudo mas invisivel ao filtro do quiz, que so sabe filtrar por tag).

Ordena os blocos pelo peso esperado (Apendice A / 19-mapa-prova.tex).
Uso:  ./cobertura.py            # relatorio completo
      ./cobertura.py --csv      # linha por subtopico, para planilha
      ./cobertura.py java bi    # so esses blocos
Nao altera nada: e leitura pura.
"""
import json, re, sys, unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CAPS = RAIZ / "apostila" / "capitulos"

# --- capitulo .tex -> tag(s) do banco. None = nao ha tag propria (gap conhecido).
CAP_TAG = {
    "02-eng-software":  ["eng-software"],
    "03-padroes-uml":   None,            # sem tag: cai em eng-software/arquitetura
    "04-arquitetura":   ["arquitetura"],
    "05-banco-dados":   ["banco-dados"],
    "06-bi":            ["bi"],
    "07-seguranca":     ["seguranca"],
    "08-programacao":   ["programacao"],
    "09-java":          ["java"],
    "10-frontend":      ["frontend"],
    "11-governanca":    ["governanca"],
    "12-redes":         ["redes"],
    "13-orfaos":        ["orfaos"],
    "14-portugues":     ["portugues"],
    "15-ingles":        ["ingles"],
    "16-rlm":           ["rlm"],
    "17-atualidades":   ["atualidades"],
    "18-legislacao":    ["legislacao"],
}

# --- peso esperado do bloco (rank menor = mais pesado). Fonte: 19-mapa-prova.tex
# (distribuicao real Modulo II 2024 + secao "Onde investir o tempo de revisao"
#  + pesos do Modulo I). Usado so para ordenar o relatorio.
PESO_RANK = {
    "eng-software": 1, "banco-dados": 2, "arquitetura": 3, "seguranca": 4,
    "programacao": 5, "bi": 6, "governanca": 7, "frontend": 8, "java": 9,
    "redes": 10,
    # Modulo I (gerais): portugues e ingles pesam 12q cada, mas peso 1.
    "portugues": 11, "ingles": 12, "atualidades": 13, "legislacao": 14, "rlm": 15,
    "orfaos": 16,
}

STOP = set("""a o e de da do das dos que com sem para por em no na nos nas um uma
uns umas ao aos as os se sua seu suas seus como qual quais entre sobre ou nao
the of and to in a is are com sem via ate cada mais menos muito pouco quando onde
seus suas ser esta este isso aquilo tem ha he la""".split())

def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                    if unicodedata.category(c) != "Mn")

def norm(s):
    return strip_accents(s).lower()

def clean_tex(s):
    """Tira comandos LaTeX deixando o texto legivel para extrair keywords."""
    s = re.sub(r"\\(textbf|emph|texttt|textit)\{([^{}]*)\}", r"\2", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)   # outros comandos
    s = s.replace("{", " ").replace("}", " ").replace("$", " ")
    s = s.replace("\\", " ")
    return re.sub(r"\s+", " ", s).strip()

def keywords_from(title, body):
    """Keywords candidatas de um subtopico: frases em \\textbf{} do corpo
    (multi-palavra = alta precisao) + palavras distintivas do titulo. Cada
    keyword e normalizada (sem acento, minuscula). O filtro de frequencia
    (dropar as genericas demais) e aplicado depois, em build_keyword_df."""
    kws = []
    for m in re.findall(r"\\textbf\{([^{}]+)\}", body):
        t = clean_tex(m)
        # separa "A x B" e "A / B" em keywords distintas
        for part in re.split(r"\s*(?: x |×|/|,|;|→|↔|–)\s*", t):
            part = part.strip(" -")
            if len(part) >= 4 and norm(part) not in STOP:
                kws.append(norm(part))
    # titulo: guarda o titulo INTEIRO (sem parentetico) como frase precisa,
    # e tambem cada palavra distintiva solta como rede de seguranca.
    ti = clean_tex(title)
    ti = re.sub(r"\([^)]*\)", "", ti).strip()
    if len(ti.split()) >= 2 and len(ti) >= 5:
        kws.append(norm(ti))
    for w in re.findall(r"[A-Za-zÀ-ÿ][\w\-]{3,}", ti):
        if norm(w) not in STOP:
            kws.append(norm(w))
    # dedup preservando ordem
    seen, out = set(), []
    for k in kws:
        if k not in seen:
            seen.add(k); out.append(k)
    return out

def parse_chapter(path):
    """Retorna (titulo_cap, [subtopicos]) onde cada subtopico e dict com
    title, section (contexto), keywords. Folha = uma subsecao, OU uma secao
    que nao tem subsecao logo abaixo dela (misturar os dois num mesmo cap e
    comum: cap com 7 secoes + 1 subsecao mantem as 6 secoes puras como folha)."""
    txt = path.read_text(encoding="utf-8")
    chap = re.search(r"\\chapter\{([^{}]*)\}", txt)
    chap_title = clean_tex(chap.group(1)) if chap else path.stem
    marks = []
    for m in re.finditer(r"\\(section|subsection)\{([^{}]*)\}", txt):
        marks.append((m.group(1), m.group(2), m.start(), m.end()))
    subs = []
    cur_section = ""
    for i, (lvl, title, s0, s1) in enumerate(marks):
        body = txt[s1: marks[i+1][2]] if i+1 < len(marks) else txt[s1:]
        if lvl == "section":
            cur_section = clean_tex(title)
            has_child = i+1 < len(marks) and marks[i+1][0] == "subsection"
            if has_child:
                continue   # esta secao vira contexto; as folhas sao as subsecoes
        subs.append({
            "title": clean_tex(title),
            "section": cur_section if lvl == "subsection" else clean_tex(title),
            "keywords": keywords_from(title, body),
        })
    return chap_title, subs

def load_banks():
    b1 = json.load(open(RAIZ / "banco.json", encoding="utf-8"))
    b2 = json.load(open(RAIZ / "banco-provas.json", encoding="utf-8"))
    qs = []
    for src, bank in (("orig", b1), ("prova", b2)):
        for q in bank:
            blob = " ".join([q.get("q", "")] + q.get("alts", [])
                            + [q.get("why", "")]
                            + list((q.get("erradas") or {}).values()))
            qs.append({"tag": q.get("tag", "?"), "src": src, "blob": norm(blob)})
    return qs

def build_df(subs_by_cap, qs):
    """Frequencia de documento de cada keyword candidata no banco inteiro."""
    cand = set()
    for subs in subs_by_cap.values():
        for st in subs:
            cand.update(st["keywords"])
    df = {}
    for k in cand:
        df[k] = sum(1 for q in qs if k in q["blob"])
    return df

# keyword de UMA palavra que bate em mais que isto (fracao do banco) e generica
GEN_FRAC = 0.05

def usable_keywords(kws, df, n_total):
    lim = GEN_FRAC * n_total
    out = [k for k in kws if (" " in k) or df.get(k, 0) <= lim]
    return out or kws   # se sobrou nada, cai pro conjunto bruto (e sinaliza fora)

def count_matches(kws, qs, tags, df, n_total):
    """(n_no_bloco, n_qualquer, n_kw_usadas) usando so keywords distintivas."""
    ku = usable_keywords(kws, df, n_total)
    if not ku:
        return 0, 0, 0
    in_block = any_tag = 0
    for q in qs:
        if not any(k in q["blob"] for k in ku):
            continue
        any_tag += 1
        if tags and q["tag"] in tags:
            in_block += 1
    return in_block, any_tag, len(ku)

def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_csv = "--csv" in sys.argv
    qs = load_banks()
    n_total = len(qs)
    subs_by_cap = {cap: parse_chapter(CAPS / f"{cap}.tex")[1] for cap in CAP_TAG}
    df = build_df(subs_by_cap, qs)
    caps = sorted(CAP_TAG)
    # ordena por peso do bloco
    def rank(cap):
        tags = CAP_TAG[cap]
        if not tags:
            return PESO_RANK.get("eng-software", 99) - 0.5  # padroes-uml junto do topo
        return min(PESO_RANK.get(t, 99) for t in tags)
    caps.sort(key=rank)

    if as_csv:
        print("bloco;peso_rank;subtopico;secao;n_no_bloco;n_qualquer_tag;n_kw;keywords")
    for cap in caps:
        tags = CAP_TAG[cap]
        if argv and not any(a in cap for a in argv):
            continue
        chap_title = re.search(r"\\chapter\{([^{}]*)\}",
                               (CAPS / f"{cap}.tex").read_text(encoding="utf-8"))
        chap_title = clean_tex(chap_title.group(1)) if chap_title else cap
        subs = subs_by_cap[cap]
        tagset = set(tags) if tags else None
        rows = []
        for st in subs:
            nb, na, nk = count_matches(st["keywords"], qs, tagset, df, n_total)
            rows.append((st, nb, na, nk))
        if as_csv:
            for st, nb, na, nk in rows:
                ku = usable_keywords(st["keywords"], df, n_total)
                print(f'{cap};{rank(cap)};{st["title"]};{st["section"]};'
                      f'{nb};{na};{nk};{"|".join(ku[:8])}')
            continue
        tag_lbl = "/".join(tags) if tags else "SEM TAG (cai em eng-software/arquitetura)"
        print(f"\n{'='*74}\n{cap}  ->  tag: {tag_lbl}")
        total_tag = sum(1 for q in qs if tagset and q["tag"] in tagset)
        print(f"{chap_title}   |   {len(subs)} subtopicos   |   "
              f"{total_tag} questoes sob essa tag")
        print(f"{'-'*74}")
        print(f"{'subtopico':<40} {'bloco':>5} {'qualq':>5}   sinal")
        for st, nb, na, nk in sorted(rows, key=lambda r: (r[2], r[1])):
            if na == 0:
                flag = "!! DESCOBERTO (0 questoes)"
            elif tagset and nb == 0:
                flag = f">> gap de TAG ({na}q existem, 0 sob a tag)"
            elif na <= 3:
                flag = "raro (<=3q)"
            elif tagset and nb <= 2 and na >= 6:
                flag = f"gap parcial de tag ({nb} sob tag / {na} no total)"
            else:
                flag = ""
            print(f"{st['title'][:39]:<40} {nb:>5} {na:>5}   {flag}")
    print("\n(bloco = questoes sob a tag do capitulo; qualq = em qualquer tag, "
          "por palavra-chave distintiva)")

if __name__ == "__main__":
    main()
