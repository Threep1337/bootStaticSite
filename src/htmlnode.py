


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
    


def main():
    node = LeafNode(None, "Hello, world!")
    print(node)
    print(node.to_html())

if __name__ == "__main__":
    main()