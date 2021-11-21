-- Create admins table 
CREATE TABLE admins (
  ID int NOT NULL,
  NAME varchar(50) NOT NULL,
  PHONE varchar(10) NOT NULL,
  PWD varchar(100) NOT NULL
);

--
-- Dumping data for table admins
--

INSERT INTO admins (ID, NAME, PHONE, PWD) VALUES
(1, 'your_name', 'your_user_id', 'YourPassword');

-- --------------------------------------------------------

--
-- Table structure for table developers
--

CREATE TABLE developers (
  NAME varchar(50) NOT NULL,
  EMAIL varchar(100) NOT NULL,
  PHONE varchar(10) NOT NULL,
  CITY varchar(30) NOT NULL,
  AGE int NOT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table verified_devs
--

CREATE TABLE verified_devs (
  NAME varchar(100) NOT NULL,
  EMAIL varchar(50) NOT NULL,
  PHONE varchar(10) NOT NULL,
  CITY varchar(50) NOT NULL,
  AGE int NOT NULL,
  PWD varchar(15) NOT NULL
);

-- Setting admins table unique and primary keys

ALTER TABLE admins
  ADD PRIMARY KEY(ID,PHONE)

--
-- Indexes for table developers
--
ALTER TABLE developers
  ADD primary KEY(PHONE,EMAIL)

--
-- Indexes for table verified_devs
--
ALTER TABLE verified_devs
  ADD PRIMARY KEY (PHONE);

COMMIT;
