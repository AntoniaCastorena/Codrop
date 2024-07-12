import HashMap "mo:base/HashMap";
import Iter "mo:base/Iter";
import Nat32 "mo:base/Nat32";
import Text "mo:base/Text";
import Principal "mo:base/Principal";
import Debug "mo:base/Debug";

actor Riego{
  type User={
    nombre: Text;
  };
  type Riego ={
    tipo_tierra: Text;
    tipo_cultivo: Text;
    hectarea: Nat32;
  }
  
};
