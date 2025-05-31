import argparse
from time import sleep

import EasyMCP2221


def main():
    parser = argparse.ArgumentParser(
        prog='mcp2221-gpio-set-output',
        description=('Set a state on a given GPIO output to a declared value of the '
                     'first found MCP2221.')
    )
    parser.add_argument("-g", "--gpio",
                        nargs="+",
                        choices=(0, 1, 2, 3),
                        required=True)
    parser.add_argument("-s", "--state",
                        nargs="+",
                        choices=(0, 1),
                        required=True)
    args = parser.parse_args()

    mcp = EasyMCP2221.Device()

    if len(args.state) != len(args.gpio):
        raise ValueError("The number of the given GPIOs needs to be equal to the "
                         "number of states.")

    gpio_dir_map = {}
    gpio_state_map = {}
    for gpio, state in zip(args.gpio, args.state):
        gpio_dir_map[f"gp{gpio}"] = "GPIO_OUT"
        gpio_state_map[f"gp{gpio}"] = state

    mcp.set_pin_function(**gpio_dir_map)
    mcp.GPIO_write(**gpio_state_map)


if __name__ == "__main__":
    main()
