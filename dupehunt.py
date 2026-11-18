#!/usr/bin/env python3
"""dupe-hunt: lista arquivos duplicados (mesmo tamanho e SHA-256). Nunca apaga nada."""
import hashlib, os, sys, collections
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def achar(raiz):
    por_tam = collections.defaultdict(list)
    for d, _, fs in os.walk(raiz):
        for n in fs:
            p = os.path.join(d, n)
            if os.path.isfile(p) and not os.path.islink(p): por_tam[os.path.getsize(p)].append(p)
    grupos = collections.defaultdict(list)
    for tam, ps in por_tam.items():
        if len(ps) > 1 and tam > 0:
            for p in ps: grupos[sha(p)].append(p)
    return [g for g in grupos.values() if len(g) > 1]
if __name__ == "__main__":
    gs = achar(sys.argv[1] if len(sys.argv) > 1 else ".")
    for g in gs: print("\n".join(g), end="\n\n")
    print(f"{len(gs)} grupo(s) de duplicados")
