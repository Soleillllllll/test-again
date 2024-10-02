import matplotlib.pyplot as plt
import networkx as nx

# 创建一个有向图
G = nx.DiGraph()

# 添加节点和边
G.add_edge('Newton-Leibniz formula', 'Differential/Derivative')
G.add_edge('Newton-Leibniz formula', 'limit')
G.add_edge('Newton-Leibniz formula', 'integral')


G.add_edge('Differential/Derivative', 'definition(chapter2)')
G.add_edge('limit', 'definition(chapter1)')
G.add_edge('integral', 'definition(chapter5)')

G.add_edge('definition(chapter5)', 'operation(chapter4)')
G.add_edge('definition(chapter2)', 'operation(chapter2)')
G.add_edge('definition(chapter1)', 'operation(chapter1)')

G.add_edge('operation(chapter4)', 'apply(chapter6)')
G.add_edge('operation(chapter2)', 'apply(chapter3,2)')
G.add_edge('operation(chapter1)', 'apply(chapter1)')


G.add_edge('apply(chapter1)', 'continuous function')
G.add_edge('apply(chapter3,2)', 'continuous function')
G.add_edge('apply(chapter6)', 'continuous function')







# 设置节点位置
pos = {
    'Newton-Leibniz formula': (0, -2.5),
    'Differential/Derivative': (1, -1),
    'limit': (1, -2.5),
    'integral': (1, -3.5),
    'definition(chapter2)': (2, -1),
    'definition(chapter1)': (2, -2.5),
    'definition(chapter5)': (2, -3.5),
    'operation(chapter4)': (3, -3.5),
    'operation(chapter1)': (3, -2.5),
    'operation(chapter2)': (3, -1),
    'apply(chapter1)': (4, -2.5),
    'apply(chapter6)': (4, -3.5),
    'apply(chapter3,2)': (4, -1),
    'continuous function': (5, -2.5),

}

# 绘制图形
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, arrows=True)

# 显示图形
plt.show()