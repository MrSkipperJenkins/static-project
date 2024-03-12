from textnode import TextNode


def main():
  print("Starting Site Generator...")

  my_first_node = TextNode("This is some smaple text", "bold", "https://www.boot.dev")

  my_first_node.repr()

main()
