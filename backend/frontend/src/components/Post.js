function Post(){
    let items=[]
    for (let i = 0; i < 8; i++) {
        items.push(<div>I am a post</div>);
    }
    return(
        <h1>
            {items}
        </h1>
    );
}
export default Post;