import turtle as t


def main():
    t.color("green")
    t.bgcolor("black")
    t.speed("fastest")

    for b in range(200):
        t.right(b)
        t.forward(b * 3)

    t.done()


if __name__ == "__main__":
    main()
