# remove duplicate primary keys from sql file.
import hashlib

output_file_path = "/mnt/c/Users/David/Downloads/dsmrreader/dsmr_out.txt"
input_file_path = "/mnt/c/Users/David/Downloads/dsmrreader/dsmr_in.txt"

completed_ids_hash = set()

output_file = open(output_file_path, "w")

for line in open(input_file_path, "r"):
  rowid = line.split()[0]
 
  hashValue = hashlib.md5(rowid.rstrip().encode('utf-8')).hexdigest()
 
  if hashValue not in completed_ids_hash:
    output_file.write(line)
    completed_ids_hash.add(hashValue)
  else:
    print(rowid)

output_file.close()
