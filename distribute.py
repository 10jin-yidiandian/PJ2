def split_file(input_file, num_files):
    # 读取原始数据
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # 计算每个文件应该包含的行数
    num_lines_per_file = len(lines) // num_files

    # 分割数据并写入到对应文件
    for i in range(num_files):
        output_file = f"FA_list_all_{i}.txt"
        start_idx = i * num_lines_per_file
        end_idx = start_idx + num_lines_per_file if i < num_files - 1 else None
        with open(output_file, 'w') as f:
            f.writelines(lines[start_idx:end_idx])

# 调用函数将数据分割成八份
split_file("FA_list_all.txt", 8)
print("data is distributed")