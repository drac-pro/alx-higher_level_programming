#!/usr/bin/python3
""""""


def print_stats(size, status_codes):
    """prints those statistics
    Args:
        size (int): combine file size
        status_codes (dict): status_code/count
    """
    print("File size: {}".format(size))
    for scode, count in status_codes.items():
        if count > 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
                    '405': 0, '500': 0}
    size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count != 0 and line_count % 10 == 0:
                print_stats(size, status_codes)

            parts = line.split()

            try:
                if parts[-2] in status_codes.keys():
                    status_codes[parts[-2]] += 1
                except Exception:
                    pass
            try:
                size += int(parts[-1])
            except Exception:
                pass
            line_count += 1
        print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
