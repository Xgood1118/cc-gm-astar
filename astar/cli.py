import argparse
import astar as m


def main():
    ap = argparse.ArgumentParser(description="动态障碍寻路")
        ap.add_argument("--from", dest="src", required=True)
        ap.add_argument("--to", dest="dst", required=True)
        ap.add_argument("--out", required=True)
    a = ap.parse_args()
        print("TODO")


if __name__ == "__main__":
    main()
