# pylint: disable=invalid-name
"""
3次元曲面を描画するスクリプト
"""
from typing import cast
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # type: ignore


plt.rcParams["font.family"] = "Meiryo"
plt.rcParams["font.size"] = 12


def surface_setting(x, y):
    """
    描画する曲面の関数を定義する関数
    """
    r = 5
    z = np.where(x**2 + y**2 <= r**2, np.sqrt(r**2 - x**2 - y**2), np.nan)
    return z


def draw_surface():
    """
    3次元曲面を描画する関数
    """
    fig = plt.figure(figsize=(10, 8))
    ax = cast(Axes3D, fig.add_subplot(111, projection="3d"))

    # x, y の範囲を設定する
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    X, Y = np.meshgrid(x, y)
    Z = surface_setting(X, Y)

    # 曲面を描画する
    surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
    ax.set_title("3次元曲面の描画", fontsize=16)
    ax.set_xlabel("X軸")
    ax.set_ylabel("Y軸")
    ax.set_zlabel("Z軸")

    # 曲面の色を設定する
    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.tight_layout()
    plt.show()


def main():
    """
    メイン関数
    """
    draw_surface()


if __name__ == "__main__":
    main()
