import meshio

def ply_to_obj(input_file, output_file):
    # 读取PLY文件
    mesh = meshio.read(input_file)

    # 写入OBJ文件
    meshio.write(output_file, mesh, file_format='obj')

# 调用函数转换文件
input_ply_file = '2.ply'
output_obj_file = '3.obj'

ply_to_obj(input_ply_file, output_obj_file)
