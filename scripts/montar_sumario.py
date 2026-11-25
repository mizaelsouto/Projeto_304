"""Monta o sumário com as páginas reais (duas passadas) e confere cada entrada."""
import json, os, re, subprocess, sys
cfgp = sys.argv[1] if len(sys.argv) > 1 else "config.json"
HERE = os.path.dirname(os.path.abspath(cfgp)); CFG = json.load(open(cfgp, encoding="utf-8"))
MD, PDF = os.path.join(HERE, CFG["md"]), os.path.join(HERE, CFG["pdf"])
norm = lambda t: re.sub(r"\s+", " ", t).strip()

def heads():
    s = open(MD, encoding="utf-8").read(); out = []
    for line in s[s.index("## RESUMO"):].split("\n"):
        m = re.match(r"^(##|###) (.+)$", line)
        if m and m.group(2).strip() != "RESUMO":
            out.append((len(m.group(1)), m.group(2).strip()))
    return out

def write(H, pages):
    s = open(MD, encoding="utf-8").read()
    toc = "\n".join(f"@TOC|{l}|{t}|{pages.get(k, '0')}" for k, (l, t) in enumerate(H)) + "\n"
    s = re.sub(r"(## SUMÁRIO\n\n)(?:@TOC\|[^\n]*\n|@@TOC@@\n)+", lambda m: m.group(1) + toc, s)
    open(MD, "w", encoding="utf-8").write(s)

def build():
    r = subprocess.run([sys.executable, os.path.join(HERE, "gerar_relatorio.py"), cfgp], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:]); sys.exit(1)

def find(H):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
    tx = {p: [norm(l) for l in subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", PDF, "-"], capture_output=True, text=True).stdout.split("\n")] for p in range(1, n + 1)}
    start = next(p for p in tx if "RESUMO" in tx[p] and not any("SUMÁRIO" in l for l in tx[p]))
    res = {}
    for k, (l, t) in enumerate(H):
        key = norm(t)
        for p in range(start, n + 1):
            if any(x == key or (x.startswith(key[:45]) and "...." not in x) for x in tx[p]):
                res[k] = p; start = p; break
    return n, res

H = heads()
write(H, {}); build(); n, p1 = find(H)
write(H, p1); build(); n, p2 = find(H)
if p2 != p1:
    write(H, p2); build(); n, p2 = find(H)
miss = [H[k][1] for k in range(len(H)) if k not in p2]
print(f"Páginas: {n} | entradas no sumário: {len(H)} | títulos não encontrados: {miss or 'nenhum'}")
