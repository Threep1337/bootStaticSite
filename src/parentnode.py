from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode (HTMLNode):
    def __init__(self,tag,children,props = None):
        super().__init__(tag=tag,children=children,props=props)
    
    def to_html(self):
        if not self.children:
            raise ValueError("Children must be present on a parent node.")
        
        if not self.tag:
            raise ValueError()
        
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html+= child.to_html()
        html +=f"</{self.tag}>"

        return html

    def __repr__(self):
        return f"ParentNode({self.tag},{self.value},{self.children},{self.props})"

def main():

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

if __name__ == "__main__":
    main()