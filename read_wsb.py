import sys

def read_wsb(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("#WSB"):
        print("❌ WSB 파일이 아님")
        return

    print("=== WSB 정보 ===")
    for line in lines[1:]:
        print(line.strip())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("WSB 파일을 더블클릭하세요")
    else:
        read_wsb(sys.argv[1])

    input("\n엔터를 누르면 종료")
