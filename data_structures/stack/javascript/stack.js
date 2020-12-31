class Stack {
  constructor(items=null){
    this.items = items ? items : [];
  }

  isEmpty = () => this.items.length === 0

  push = (item) => this.items.push(item);

  pop = () => this.items.pop();

  peek = () => this.items[this.items.length-1];
}


