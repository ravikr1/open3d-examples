# examples/Python/Basic/python_binding.py
# https://github.com/PointCloudLibrary/data
import open3d as o3d


def example_import_function():
    pcd = o3d.io.read_point_cloud("../../TestData/ICP/cloud_bin_0.pcd")
    print(pcd)


def example_help_function():
    help(o3d)
    help(o3d.geometry.PointCloud)
    help(o3d.io.read_point_cloud)


if __name__ == "__main__":
    example_import_function()
    example_help_function()