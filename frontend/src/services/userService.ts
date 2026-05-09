import api from "./api";
import type  { User } from "../types/user"; 

export const getUsers = async (): Promise<User[]> => {
  const response = await api.get("/users");
  return response.data;
};

// Create a new user
export const createUser = async (
  name: string,
  email: string
) => {
  const response = await api.post("/users", {
    name,
    email,
  });

  return response.data;
};

// Update an existing user
export const updateUser = async (
  id: number,
  name: string,         
    email: string   
) => {
  const response = await api.put(`/users/${id}`, {
    name,
    email,
  });       

    return response.data;
};

// Delete a user
export const deleteUser = async (id: number) => {
  await api.delete(`/users/${id}`);
};  

