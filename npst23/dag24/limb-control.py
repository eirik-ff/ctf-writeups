binary = ""

def cycle_pin(pin: int, state: int = 0):
    global binary
    binary += str(state)


def usleep(delay: int):
    global binary
    binary += " "


def left_leg_control():
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0,1)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0)
    cycle_pin(0)
    cycle_pin(0)
    cycle_pin(0,1)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0,1)
    usleep(10)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0,1)
    cycle_pin(0)
    cycle_pin(0)
    cycle_pin(0,1)
    cycle_pin(0)


def right_arm_control():
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,0)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,1)
    usleep(10)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,1)
    cycle_pin(3,0)
    cycle_pin(3,0)
    cycle_pin(3,1)

def right_leg_control():
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1,0)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1,0)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    usleep(10)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1,0)
    cycle_pin(1,0)
    cycle_pin(1)
    cycle_pin(1)
    cycle_pin(1)

def left_arm_control():
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,0)
    cycle_pin(2,1)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,1)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,0)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,1)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,1)
    usleep(10)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,1)
    cycle_pin(2,0)
    cycle_pin(2,0)
    cycle_pin(2,1)
    cycle_pin(2,0)


def main():
    global binary

    left_leg_control()
    right_arm_control()
    right_leg_control()
    left_arm_control()

    numbers = []
    for b in binary.split(" "):
        n = int(b, 2)
        numbers.append(n)

    output = b""
    for n in numbers:
        output += n.to_bytes((n.bit_length() + 7 ) // 8, "big")

    print(output.decode("latin-1"))


if __name__ == "__main__":
    main()

