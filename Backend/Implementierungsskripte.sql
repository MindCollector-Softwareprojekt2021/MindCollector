/*==============================================================*/
/* DBMS name:      ORACLE Version 19c                           */
/* Created on:     04.05.2021 12:39:36                          */
/*==============================================================*/


alter table EINTRAG
   drop constraint FK_EINTRAG_RELATIONS_KATEGORI;

alter table KATEGORIE
   drop constraint FK_KATEGORI_RELATIONS_USERACCO;

alter table RELATIONSHIP_9
   drop constraint FK_RELATION_BESITZT_KATEGORI;

alter table RELATIONSHIP_9
   drop constraint FK_RELATION_HAT_USERACCO;

drop table EINTRAG cascade constraints;

drop index RELATIONSHIP_12_FK;

drop table KATEGORIE cascade constraints;

drop index BESITZT_FK;

drop index HAT_FK;

drop table RELATIONSHIP_9 cascade constraints;

drop table USERACCOUNT cascade constraints;

/*==============================================================*/
/* Table: EINTRAG                                               */
/*==============================================================*/
create table EINTRAG (
   EINTRAG_ID           INTEGER               not null,
   KATEGORIE_ID         INTEGER               not null,
   EINTRAG_TITEL        CHAR(50)              not null,
   EINTRAG_BESCHREIBUNG TEXT                  not null,
   AUDIO                BLOB,
   AUDIOTEXT            TEXT,
   BILD                 BLOB,
   constraint PK_EINTRAG primary key (EINTRAG_ID)
);

/*==============================================================*/
/* Table: KATEGORIE                                             */
/*==============================================================*/
create table KATEGORIE (
   KATEGORIE_ID         INTEGER               not null,
   USER_ID              INTEGER               not null,
   KATEGORIE_TITEL      CHAR(50)              not null,
   constraint PK_KATEGORIE primary key (KATEGORIE_ID)
);

/*==============================================================*/
/* Index: RELATIONSHIP_12_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_12_FK on KATEGORIE (
   USER_ID ASC
);

/*==============================================================*/
/* Table: RELATIONSHIP_9                                        */
/*==============================================================*/
create table RELATIONSHIP_9 (
   USER_ID              INTEGER               not null,
   KATEGORIE_ID         INTEGER               not null,
   constraint PK_RELATIONSHIP_9 primary key (USER_ID, KATEGORIE_ID)
);

/*==============================================================*/
/* Index: HAT_FK                                                */
/*==============================================================*/
create index HAT_FK on RELATIONSHIP_9 (
   USER_ID ASC
);

/*==============================================================*/
/* Index: BESITZT_FK                                            */
/*==============================================================*/
create index BESITZT_FK on RELATIONSHIP_9 (
   KATEGORIE_ID ASC
);

/*==============================================================*/
/* Table: USERACCOUNT                                           */
/*==============================================================*/
create table USERACCOUNT (
   USER_ID              INTEGER               not null,
   VORNAME              CHAR(50)              not null,
   NACHNAME             CHAR(50)              not null,
   EMAIL                CHAR(50)              not null,
   PASSWORT             CHAR(50)              not null,
   SICHERHEITSFRAGE1    TEXT                  not null,
   SICHERHEITSANTWORT1  TEXT                  not null,
   SICHERHEITSFRAGE2    TEXT                  not null,
   SICHERHEITSANTWORT2  TEXT                  not null,
   CREATED_AT           DATE,
   constraint PK_USERACCOUNT primary key (USER_ID)
);

alter table EINTRAG
   add constraint FK_EINTRAG_RELATIONS_KATEGORI foreign key (KATEGORIE_ID)
      references KATEGORIE (KATEGORIE_ID);

alter table KATEGORIE
   add constraint FK_KATEGORI_RELATIONS_USERACCO foreign key (USER_ID)
      references USERACCOUNT (USER_ID);

alter table RELATIONSHIP_9
   add constraint FK_RELATION_BESITZT_KATEGORI foreign key (KATEGORIE_ID)
      references KATEGORIE (KATEGORIE_ID);

alter table RELATIONSHIP_9
   add constraint FK_RELATION_HAT_USERACCO foreign key (USER_ID)
      references USERACCOUNT (USER_ID);

