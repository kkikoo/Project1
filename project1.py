from pathlib import Path

code_of_message_type = {1:"CANCELLATION", -1:"CANCELLATION", 2:"ALERT", -2:"ALERT"}

def add_message(time, device_id, message_type, message_name, from_device):
    return time,device_id, message_type, message_name, from_device

def my_sort(ls):
    y = sorted(ls, key = lambda ele: (ele[0], ele[1], ele[2], ele[3], ele[4]))
    return y

def print_sent(time, device_id, message_type, to_id, message_name):
    print ("@{} #{}: SENT {} TO #{}: {}".format(time, device_id, code_of_message_type[message_type], to_id, message_name))

def print_received(time, device_id, message_type, from_id, message_name):
    print ("@{} #{}: RECEIVED {} TO #{}: {}".format(time, device_id, code_of_message_type[message_type], from_id, message_name))



def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())

def process_file(filepath):
    device = []
    next_device = {}
    cost_of_time = {}
    all_message_name = set()
    message_list = []

    try:
        #print filepath
        with open(filepath, 'r') as f:
            for line in f.readllines():
                line - line.strip()
                if len(line) == 0 or line[0] == '#':
                    continue
                word = line.split(' ')
                #print word
                if word[0] == 'DEVICE':
                    device.append(int(word[1]))
                elif word[0] == "PROPAGATE":


def main() -> None:
    """Runs the simulation program in its entirety"""
    input_file_path = _read_input_file_path()


if __name__ == '__main__':
    main()
