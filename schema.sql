create sequence AUTO_ID;

create table company(
id_company integer primary key DEFAULT nextval('AUTO_ID') not null,
name_company varchar(255) not null,
trade_c varchar(255) not null,
address varchar(255) not null,
name_responsible varchar(255) not null,
email varchar(150) not null,
password_company text not null,
descri text, 
logo varchar(255),
cnpj varchar(64) not null 
);
create table applicant(
	id_applicant integer primary key DEFAULT nextval('AUTO_ID') not null,
	name_candidate varchar(255) not null,
	cpf varchar(11) not null,
	email_applicant varchar(200) not null,
	password text not null
	);
create table type_plan(
	id_type_plan integer primary key DEFAULT nextval('AUTO_ID') not null,
	name_plan varchar(150) not null,
	pricing numeric(100,2)
	);


create table company_plan(
	id_company_plan integer primary key DEFAULT nextval('AUTO_ID') not null,
	id_type_plan integer references type_plan(id_type_plan),
	id_company integer references company(id_company),
	date_register date
	);

create table payment_company(
	id_payment_company integer primary key DEFAULT nextval('AUTO_ID') not null,
	id_company_plan integer references company_plan(id_company_plan),
	date_payment date
);
create table applicant_wave(
	id_applicant_ware integer primary key DEFAULT nextval('AUTO_ID') not null,
	id_applicant integer references applicant(id_applicant) not null,
	id_ware varchar(255) not null,
	selected_applicant boolean,
	data_candidacy date not null
	);
create table videoconference_date(
	id_videoconference_date integer primary key DEFAULT nextval('AUTO_ID') not null,
	id_applicant integer references applicant(id_applicant),
	id_company integer references company(id_company),
	date_video timestamp not null,
	url_videoconderence varchar(255) 
	);

---Funções

create function insertApplicant()