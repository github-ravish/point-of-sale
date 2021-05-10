import base64
from io import BytesIO
import matplotlib.pyplot as plt

class Matplotlib():

	def get_graph(self):
		buffer = BytesIO()
		plt.savefig(buffer, format='png')
		buffer.seek(0)
		image_png = buffer.getvalue()
		graph = base64.b64encode(image_png)
		graph = graph.decode('utf-8')
		buffer.close()
		return graph

	def get_chart(self, data, **kwargs):
		plt.switch_backend('AGG')
		fig = plt.figure(figsize=(10, 4))
		plt.bar(data['order_id'], data['price'])
		plt.tight_layout()
		chart = self.get_graph()
		return chart