import unittest

from htmlnode import HTMLNode

# , text_type_bold, text_type_code,
#                       text_type_image, text_type_italic, text_type_link,
#                       text_type_text)


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "This is some test text value", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "This is some test text value", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("a", "This is some test text value" , None, {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "This is some other test text value" , None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode("This is a text node")
        node2 = HTMLNode("This is a text node2")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = HTMLNode("This is a text node", "https://www.boot.dev")
        node2 = HTMLNode("This is a text node", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("This is a text node", "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))    

    def test_props_to_html(self):
        node = HTMLNode("This is a text node", "https://www.boot.dev", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html) 


if __name__ == "__main__":
    unittest.main()
