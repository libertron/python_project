def go():
    a=True
    while a:
        nbre=input(">_ ")
        try:
            nbre=int(nbre)
            assert nbre < 6
            nbre=nbre/nbre
        except AssertionError:
            print("Number should be upper than 6")
        except ValueError:
            print("you should enter a number...")
        except ZeroDivisionError:
            print("No Zero Division is able in math")
        else:
            print("New number is {}".format(nbre))
            a=False