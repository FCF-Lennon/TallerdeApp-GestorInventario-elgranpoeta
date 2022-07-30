/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     11-07-2022 9:09:47                           */
/*==============================================================*/


drop table if exists Bodega;

drop table if exists Editorial;

drop table if exists Usuario;

drop table if exists Genero;

drop table if exists Libro;

/*==============================================================*/
/* Table: Bodega                                                */
/*==============================================================*/
create table Bodega
(
   bodegaID      int not null auto_increment,
   nombre        varchar(254),
   primary key (bodegaID)
);

alter table bodega auto_increment=10;

insert into bodega (bodegaID, nombre) VALUES
(1, 'Bodega A'),
(2, 'Bodega B');

/*==============================================================*/
/* Table: Editorial                                             */
/*==============================================================*/
create table editorial
(
   editorialID     int not null auto_increment,
   nombre     varchar(254),
   primary key (editorialID)
);

alter table editorial auto_increment=20;

insert into editorial (editorialID, nombre) VALUES
(1, 'Alquimia'),
(2, 'Cuneta'),
(3, 'Hueders'),
(4, 'Edicola');

/*==============================================================*/
/* Table: Usuario                                             */
/*==============================================================*/
create table usuario
(
   nombre      varchar(254),
   correo       varchar(254),
   password  varchar(254),
   rut  varchar(254),	
   estado   int,
   admin   int,
   primary key (rut)
);

INSERT INTO usuario (nombre, correo, password, rut, estado, admin) VALUES
('Ruben', '11', '11', '17239883-5', 1, 1),
('Felipe', 'FelipeCarrasco@inacapmail.cl', '1234', '17283634-k', 1, 0),
('Cristobal', 'CristobalCortes@inacapmail.cl', '1234', '19293984-9', 0, 0),
('Sebastian', 'SebastianRamirez@inacapmail.cl', '1111', '20133789-5', 1, 1),
('Maria Fernanda', 'MariaFernandaDiaz@inacapmail.cl', '1234', '20347383-1', 1, 0),
('Diego', 'DiegoEsquivel@inacapmail.cl', '1111', '20654838-6', 1, 1),
('Amit', 'AmitMartinez@inacapmail.cl', '1111', '21288571-1', 1, 1);


/*==============================================================*/
/* Table: Categoria                                                */
/*==============================================================*/
create table categoria
(
   categoriaID   int not null auto_increment,
   nombre        varchar(254),
   primary key (categoriaID)
);

alter table categoria auto_increment=30;

insert into categoria (categoriaID, nombre) VALUES
(1, 'Shonen'),
(2, 'Seinen'),
(3, 'Kodomo'),
(4, 'Ecchi'),
(5, 'Shojo'),
(6, 'Josei'),
(7, 'Mecha'),
(8, 'Deportes'),
(9, 'Gore'),
(10, 'FantasÃ­a'),
(11, 'Guerra'),
(12, 'Horror'),
(13, 'Lucha'),
(14, 'Magia'),
(15, 'Misterio'),
(16, 'Post Apocaliptico '),
(17, 'Samurai'),
(18, 'Shooter'),
(19, 'Shounen'),
(20, 'Shoujo'),
(21, 'Kemono');

/*==============================================================*/
/* Table: Libro                                            */
/*==============================================================*/
create table libro
(
   codigo          int not null auto_increment,
   categoriaID      int not null,
   editorialID      int not null,
   nombre      	varchar(254),
   autor 	varchar(254),
   stock       	int,
   bodegaID	int not null,
   primary key (codigo)
);


alter table libro auto_increment=40;

insert into libro (codigo, categoriaID, editorialID, nombre, autor, stock, bodegaID) VALUES
(1, 1, 1, 'Antagonista', 'Saikomic', 10, 1),
(2, 1, 1, 'One Piece', 'Echiro Oda', 20, 2),
(23, 2, 2, 'Tokyo Ghoul', 'Sui Ishida', 30, 2),
(24, 2, 3, 'Death Note', 'Tsugumi Oba', 40, 1),
(25, 3, 4, 'Doraemon', 'Fujiko Fujio', 50, 2),
(26, 3, 2, 'Hamtaro', 'Ritsuko Kawai', 60, 1),
(43, 2, 4, 'Berserk', 'Kentaro Miura', 60, 1);


alter table libro add constraint FK_escrito foreign key (bodegaID)
      references bodega (bodegaID) on delete restrict on update restrict;

alter table libro add constraint FK_impreso foreign key (editorialID)
      references editorial (editorialID) on delete restrict on update restrict;

alter table libro add constraint FK_tiene foreign key (categoriaID)
      references categoria (categoriaID) on delete restrict on update restrict;












