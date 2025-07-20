

from textnode import TextNode,TextType
class HTMLNode():
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        html = ""
        if self.props:
            for attribute,value in self.props.items():
                html += f" {attribute}=\"{value}\""
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props = None):
        super().__init__(value=value,tag=tag,props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError()
        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"
    
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
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            return LeafNode("a",text_node.text,{"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        case _:
            raise ValueError("text node has an invalid text type!")


# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(text_type,TextType):
        raise ValueError("Invalid text type.")
    
    new_nodes = []

    #print(f"****length of old nodes is {len(old_nodes)}****")

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception ("Unable to find matching delimeters, markdown is invalid.")
            
            for x in range (0, len(split_text)):
                if x % 2 == 0:
                    if split_text[x] != "":
                        new_nodes.append(TextNode(split_text[x],TextType.TEXT))
                else:
                    if split_text[x] != "":
                        new_nodes.append(TextNode(split_text[x],text_type))
    return new_nodes

def main():
    #test_text = TextNode("this is a test with a *bold* word",TextType.TEXT)
    #text_node_to_html_node(test_text)
    #node = LeafNode(None, "Hello, world!")
    #print(node)
    #print(node.to_html())
    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

    for node in new_nodes:
        print (node)

if __name__ == "__main__":
    main()