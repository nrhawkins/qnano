from collections import defaultdict

def reorder_log_entries(log_lines):

    new_log = list()
    log_numbers = list()
    log_text = defaultdict(list)

    for log_line in log_lines:
        words = log_line.split(" ")
        if len(words) >= 2:
            if words[1].isnumeric():
                log_numbers.append(log_line)
            else:
                index_log_body = log_line.find(" ") + 1
                log_text[log_line[index_log_body:]].append(words[0])
        else:
            # malformed log line, drop from the new log
            pass

    for log_body in sorted(list(log_text.keys())):
        log_ids = sorted(list(log_text[log_body]))
        for log_id in log_ids:
            new_log.append(log_id + " " + log_body)

    new_log = new_log + log_numbers

    return new_log



log_lines = ["a11 log1 log1 log1",
             "a1n 12 13 14",
             "a2 log2 log2 log2",
             "a2n 22 23 24",
             "a1 log1 log1 log1",
             "a00 log1 log1 log1",
             "b0 log0 log0 log0",
             "b0 12 12 12"
             ]

print("new log", reorder_log_entries(log_lines))

