class TextNode():
  def __init__(self, text, text_type, url):
    self.text = text
    self.text_type = text_type
    self.url = url

  def eq(self, second_node):
    return self.text == second_node.text and self.text_type == second_node.text_type and self.url == second_node.url

  def repr(self):
    print(f"TextNode({self.text}, {self.text_type}, {self.url})")
    