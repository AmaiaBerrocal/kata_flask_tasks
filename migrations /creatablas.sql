DROP TABLE IF EXISTS tareas;

CREATE TABLE "Tareas" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"titulo"	TEXT NOT NULL,
	"descripcion"	TEXT,
	"fecha"	TEXT NOT NULL
)