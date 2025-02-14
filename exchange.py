import httpx


url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025'
r = httpx.get(url)


print(r.text)
print(r.status_code)

lines = r.text.split("\n")

for line in lines:
    if "|EUR|" in line:
        row = line

print(row)

row_arr = row.split("|")

kurz_str = row_arr[-1]
kurz_str = float(kurz_str.replace(",","."))


print(kurz_str)