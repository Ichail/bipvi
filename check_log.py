from parsezeeklogs import ParseZeekLogs
import elasticsearch
with open('out.json',"w") as outfile:
    for log_record in ParseZeekLogs("conn.log.labeled", output_format="json", safe_headers=False):
        if log_record is not None:
            outfile.write(log_record + "\n")