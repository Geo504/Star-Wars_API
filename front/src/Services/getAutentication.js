export const login = async(resource, inputData) => {
  const response = await fetch(resource, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(inputData)
  })
  return response;
}