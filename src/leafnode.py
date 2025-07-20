from htmlnode import HTMLNode


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

def main():
    test = LeafNode("this is some test value",None)
    print(test)
    print(test.to_html())

if __name__ == "__main__":
    main()