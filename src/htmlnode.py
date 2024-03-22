class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def __to_html__(self):
    raise Exception(NotImplementedError)
  
  def props_to_html(self):
    html_text = ""
    
    for key, value in self.props.items():
      html_text += f' {key}="{value}"'

    print(html_text)
    return html_text

  def __repr__(self):
    return f"HTMLNode object: tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"
