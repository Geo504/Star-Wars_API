import { useEffect, useState } from "react";

import { apiCall } from "../Utils/apiCall";
// import { getResources } from "../Services/getResources";

export const useResourse = (url) => {
  const [elements, setElements]=useState([]);

  useEffect(()=>{
    const fetchData = async () => {
      const elementUrls = await apiCall(`http://localhost:5000/api/${url}/`);
      setElements(elementUrls.map(element=>({favorite: false, ...element})));
    }
    fetchData();
  }, [])

  return [elements, setElements];
}
