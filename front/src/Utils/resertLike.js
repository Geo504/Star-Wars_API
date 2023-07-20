export const resetLikes = (characters, planets, vehicles) => {
  characters.map(item=>{
    return item.favorite = false;
  })

  planets.map(item=>{
    return item.favorite = false;
  })

  vehicles.map(item=>{
    return item.favorite = false;
  })
}