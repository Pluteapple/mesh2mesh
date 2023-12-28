
# pip install pyvista
import pyvista as pv

# Load your PLY file
mesh = pv.read('2222.ply')

# Check if normals are already computed
if 'Normals' not in mesh.point_data:
    # If not present, compute the normals
    mesh.compute_normals(inplace=True)

# Now you should be able to access the normals
normals = mesh.point_data['Normals']

# Normalize the normals to use them for color mapping
normalized_normals = (normals - normals.min()) / (normals.max() - normals.min())

# Map the normalized normals to RGB colors
colors = (normalized_normals * 255).astype(int)
mesh.point_data['colors'] = colors




# Visualize the mesh with the normals as colors
plotter = pv.Plotter()

#可修改  'coolwarm'、'jet'、'viridis'
plotter.add_mesh(mesh, scalars='colors', cmap='jet')
plotter.show()
