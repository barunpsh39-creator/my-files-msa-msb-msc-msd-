import sys

def read_wsd(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("#WSD"):
        print("❌ WSD 파일이 아님")
        return

    print("=== WSD 데이터 ===")
    for line in lines[1:]:
        print(line.strip())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("WSD 파일을 더블클릭하세요")
    else:
        read_wsd(sys.argv[1])

    input("\n엔터를 누르면 종료")
