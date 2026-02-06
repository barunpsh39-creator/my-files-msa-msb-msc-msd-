import sys

def read_wsc(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("#WSC"):
        print("❌ WSC 파일이 아님")
        return

    print("=== WSC 스타일 ===")
    for line in lines[1:]:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            print(f"{key} → {value}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("WSC 파일을 더블클릭하세요")
    else:
        read_wsc(sys.argv[1])

    input("\n엔터를 누르면 종료")
