package std4

import (
	
	"fmt"
	"database/sql"
	"log"
	_ "modernc.org/sqlite"
)

func CreateDatabase() (*sql.DB, error){
	db, err := sql.Open("sqlite", "./meubanco.db")
	if err != nil{
		return nil, err
	}

	_, err = db.Exec(`
	CREATE TABLE IF NOT EXISTS usuarios(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INTEGER NOT NULL,
	cpf TEXT NOT NULL UNIQUE
	);
	`)

	if err != nil{
		fmt.Print("Erro ao criar tabela", err)
		return nil, err
	}
	log.Print("Banco criado com sucesso")
	return db, nil

}