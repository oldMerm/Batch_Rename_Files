from pathlib import Path

def count_logical_lines(path: Path) -> int:
    in_block = False
    count = 0
    for line in path.read_text(encoding='utf-8').splitlines():
        i, n = 0, len(line)
        while i < n:
            if in_block:
                if line[i:i+2] == '*/':   # 结束符
                    in_block = False
                    i += 2
                else:
                    i += 1
                continue

            if line[i].isspace():
                i += 1
                continue

            if line[i:i+2] == '//':
                break

            if line[i:i+2] == '/*':
                in_block = True
                i += 2
                continue

            count += 1
            break
    return count

if __name__ == "__main__":
    folder = input("Please enter the folder path:").strip()
    total = sum(count_logical_lines(f) for f in Path(folder).rglob('*.java'))
    print(f"The total is {total}")
