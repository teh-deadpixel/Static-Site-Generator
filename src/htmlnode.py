class HTMLNODE:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("will be overridden")
    
    def props_to_html(self):
        result = []
        if self.props is None or self.props == {}:
            return ""
        for key in self.props:
            value = self.props[key]
            result.append(f' {key}="{value}"')
        return "".join(result)
        ##for key, value in self.props.items():
            ##return f' {key} = "{value}"'
    def __repr__(self):
        return f"tag = {self.tag!r} value = {self.value!r} children = {self.children!r} props = {self.props!r})"