from pathlib import Path

code_of_message_type = {1:"CANCELLATION", -1:"CANCELLATION", 2:"ALERT", -2:"ALERT"}

def add_message(time,device_id, message_type, message_name, from_device,):
    return (time,device_id, message_type, message_name, from_device,)

def my_sort(ls):
    y = sorted(ls, key = lambda ele: (ele[0], ele[1], ele[2], ele[3], ele[4]))
    return y



def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())


def main() -> None:
    """Runs the simulation program in its entirety"""
    input_file_path = _read_input_file_path()


if __name__ == '__main__':
    main()
