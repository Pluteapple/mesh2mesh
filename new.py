import numpy as np
import pyvista as pv

# Since I can't use PyVista in this environment, I'm providing a code snippet that you can run on your local machine.

# Code to save the visualization as an image
def save_visualization(mesh, filename):
    # Check if normals are already computed
    if 'Normals' not in mesh.point_data:
        # If not present, compute the normals
        mesh.compute_normals(inplace=True)

    # Extract the normals
    normals = mesh.point_data['Normals']

    # Normalize the normals to use them for color mapping
    normalized_normals = (normals - normals.min()) / (normals.max() - normals.min())

    # Map the normalized normals to RGB colors
    colors = (normalized_normals * 255).astype(int)
    mesh.point_data['colors'] = colors

    # Visualize the mesh with the normals as colors
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, scalars='colors', cmap='coolwarm')

    # Save the screenshot
    plotter.show(screenshot=filename)

# Load your PLY file
mesh = pv.read('2222.ply')

# Save the visualization as an image file
save_visualization(mesh, 'path_to_save_image.png')

# Remember to replace 'path_to_your_ply_file.ply' with the actual path to your PLY file
# and 'path_to_save_image.png' with the path and filename where you want to save the image.
