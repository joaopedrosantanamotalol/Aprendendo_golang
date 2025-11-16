package main

import (
	"aprendendo_golang/quarto_conceito_backefront/go"
	"fmt"
	"os"
	"strconv"
	"encoding/json"
)

func main(){
	std4.Conect()

	if len(os.Args) < 2{
		fmt.Println(`{"erro":"Nenhum comando informado"}`)
	}
	switch os.Args[1]{
		case "inserir":
		nome := os.Args[2]
		idade, _ := strconv.Atoi(os.Args[3])
		cpf := os.Args[4]

		err := std4.InserirUsuario(nome, idade, cpf)
		if err != nil {
			fmt.Printf(`{"erro": "%s"}`, err)
		} else {
			fmt.Println(`{"status": "ok"}`)
		}

	case "listar":
		lista, err := std4.ListarUsuarios()
		if err != nil {
			fmt.Printf(`{"erro": "%s"}`, err)
		} else {
			json.NewEncoder(os.Stdout).Encode(lista)
		}

	case "buscar":
		id, _ := strconv.Atoi(os.Args[2])
		usuario, err := std4.BuscarPorId(id)
		if err != nil {
			fmt.Printf(`{"erro": "%s"}`, err)
		} else {
			json.NewEncoder(os.Stdout).Encode(usuario)
		}

	case "deletar":
		id, _ := strconv.Atoi(os.Args[2])
		err := std4.DeletarUsuario(id)
		if err != nil {
			fmt.Printf(`{"erro": "%s"}`, err)
		} else {
			fmt.Println(`{"status": "ok"}`)
		}

	default:
		fmt.Println(`{"erro":"comando inválido"}`)
	}
	}
