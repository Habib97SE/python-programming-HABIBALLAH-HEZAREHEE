from Geometri import Rectangle, Circle, Cube, Sphere


def main() -> None:

    cirkel1 = Circle.Circle(x=0, y=0, radius=1)  # enhetscirkel

    cirkel2 = Circle.Circle(x=1, y=1, radius=1)
    rektangel = Rectangle.Rectangle(x=0, y=0, width=1, height=1)

    print(cirkel1 == cirkel2)  # True

    print(cirkel2 == rektangel)  # False

    print(cirkel1.is_inside(0.5, 0.5))  # True

    cirkel1.translate(5, 5)

    print(cirkel1.is_inside(0.5, 0.5))  # False

    try:
        cirkel1.translate("TRE", 5)  # ge ValueError med lämplig kommentar
    except TypeError as e:
        print(e)
    finally:
        print(cirkel1)


if __name__ == "__main__":
    main()
