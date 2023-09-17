-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: fg_db
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `brands`
--

DROP TABLE IF EXISTS `brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brands` (
  `id` varchar(60) NOT NULL,
  `brand_name` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brands`
--

LOCK TABLES `brands` WRITE;
/*!40000 ALTER TABLE `brands` DISABLE KEYS */;
INSERT INTO `brands` VALUES ('00b0c138-7e8c-424f-88ab-f69ed24c5f75','Huawei'),('63d8f57f-57e4-43cf-b460-2860570af25c','Apple'),('b7b2c51e-a5eb-40ef-9535-05da233ef5f4','Samsung');
/*!40000 ALTER TABLE `brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `features`
--

DROP TABLE IF EXISTS `features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `features` (
  `id` varchar(60) NOT NULL,
  `model_id` varchar(60) NOT NULL,
  `PhoneDetails` json DEFAULT NULL,
  `NetworkDetails` json DEFAULT NULL,
  `LaunchDetails` json DEFAULT NULL,
  `BodyDetails` json DEFAULT NULL,
  `DisplayDetails` json DEFAULT NULL,
  `PlatformDetails` json DEFAULT NULL,
  `MemoryDetails` json DEFAULT NULL,
  `MainCameraDetails` json DEFAULT NULL,
  `SelfieCameraDetails` json DEFAULT NULL,
  `SoundDetails` json DEFAULT NULL,
  `CommunicationsDetails` json DEFAULT NULL,
  `FeaturesDetails` json DEFAULT NULL,
  `BatteryDetails` json DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `model_id` (`model_id`),
  CONSTRAINT `features_ibfk_1` FOREIGN KEY (`model_id`) REFERENCES `models` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `features`
--

LOCK TABLES `features` WRITE;
/*!40000 ALTER TABLE `features` DISABLE KEYS */;
INSERT INTO `features` VALUES ('383e8d93-9017-40d7-bd1a-ab9e6878539e','0653b5f6-8486-46fb-8a70-64976d513f40','{\"yearValue\": \"2022\", \"brandValue\": \"Samsung\", \"modelValue\": \"Galaxy Z Fold\"}','{\"networkSpeed\": \"HSPA 42.2/5.76 Mbps, LTE-A (7CA) Cat20 2000/200 Mbps, 5G (5+ Gbps DL)\", \"network2GBands\": \"GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (Dual SIM model only)\\\\nCDMA 800 / 1900 & TD-SCDMA\", \"network3GBands\": \"HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100\\\\nCDMA2000 1xEV-DO\", \"network4GBands\": \"1, 2, 3, 4, 5, 7, 8, 12, 13, 17, 18, 19, 20, 25, 26, 28, 32, 38, 39, 40, 41, 66 - International\\\\n1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 18, 19, 20, 25, 26, 28, 29, 30, 38, 39, 40, 41, 46, 48, 66, 71 - USA\", \"network5GBands\": \"1, 2, 3, 5, 7, 8, 12, 20, 25, 28, 38, 40, 41, 66, 75, 77, 78 SA/NSA/Sub6 - International\\\\n1, 3, 5, 7, 8, 20, 28, 38, 41, 66, 71, 260, 261 SA/NSA/Sub6/mmWave - USA\", \"networkTechnology\": \"GSM / CDMA / HSPA / EVDO / LTE / 5G\"}','{\"launchStatus\": \"Available. Released 2022, February 25\", \"launchAnnounced\": \"2022, February 09\"}','{\"bodySim\": \"Nano-SIM and eSIM or Dual SIM (2 Nano-SIMs and eSIM, dual stand-by)\", \"bodyBuild\": \"Glass front (Gorilla Glass Victus+), glass back (Gorilla Glass Victus+), aluminum frame\", \"bodyOther1\": \"IP68 dust/water resistant (up to 1.5m for 30 mins)\", \"bodyOther2\": \"Armor aluminum frame with tougher drop and scratch resistance (advertised)\", \"bodyOther3\": \"Stylus, 2.8ms latency (Bluetooth integration, accelerometer, gyro)\", \"bodyWeight\": \"228 g / 229 g (mmWave) (8.04 oz)\", \"bodyDimensions\": \"163.3 x 77.9 x 8.9 mm (6.43 x 3.07 x 0.35 in)\"}','{\"displaySize\": \"6.8 inches, 114.7 cm2 (~90.2% screen-to-body ratio)\", \"displayType\": \"Dynamic AMOLED 2X, 120Hz, HDR10+, 1750 nits (peak)\", \"displayOther1\": \"Always-On display\", \"displayProtection\": \"Corning Gorilla Glass Victus+\", \"displayResolution\": \"1440 x 3088 pixels (~500 ppi density)\"}','{\"platformOs\": \"Android 12, upgradable to Android 13, One UI 5\", \"platformCpu\": \"Octa-core (1x2.8 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.8 GHz Cortex-A510) - Europe\\\\nOcta-core (1x3.00 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.80 GHz Cortex-A510) - ROW\", \"platformGpu\": \"Xclipse 920 - Europe\\\\nAdreno 730 - ROW\", \"platformChipset\": \"Exynos 2200 (4 nm) - Europe\\\\nQualcomm SM8450 Snapdragon 8 Gen 1 (4 nm) - ROW\"}','{\"memoryOther1\": \"UFS 3.1\", \"memoryCardSlot\": \"No\", \"memoryInternal\": \"128GB 8GB RAM, 256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM\"}','{\"mainCameraQuad\": \"108 MP, f/1.8, 23mm (wide), 1/1.33\\\", 0.8µm, PDAF, Laser AF, OIS\\\\n 10 MP, f/4.9, 230mm (periscope telephoto), 1/3.52\\\", 1.12µm, dual pixel PDAF, OIS, 10x optical zoom\\\\n 10 MP, f/2.4, 70mm (telephoto), 1/3.52\\\", 1.12µm, dual pixel PDAF, OIS, 3x optical zoom\\\\n 12 MP, f/2.2, 13mm, 120˚ (ultrawide), 1/2.55\\\", 1.4µm, dual pixel PDAF, Super Steady video\", \"mainCameraVideo\": \"8K@24fps, 4K@30/60fps, 1080p@30/60/240fps, 720p@960fps, HDR10+, stereo sound rec., gyro-EIS\", \"mainCameraFeatures\": \"LED flash, Auto-HDR, panorama\"}','{\"selfieCameraVideo\": \"4K@30/60fps, 1080p@30fps\", \"selfieCameraSingle\": \"40 MP, f/2.2, 26mm (wide), 1/2.82\\\", 0.7µm, PDAF\", \"selfieCameraFeatures\": \"Dual video call, Auto-HDR\"}','{\"soundOther1\": \"32-bit/384kHz audio\", \"soundOther2\": \"Tuned by AKG\", \"sound35MmJack\": \"No\", \"soundLoudspeaker\": \"Yes, with stereo speakers\"}','{\"communicationsNfc\": \"Yes\", \"communicationsUsb\": \"USB Type-C 3.2, OTG\", \"communicationsWlan\": \"Wi-Fi 802.11 a/b/g/n/ac/6e, dual-band, Wi-Fi Direct\", \"communicationsRadio\": \"No\", \"communicationsBluetooth\": \"5.2, A2DP, LE\", \"communicationsPositioning\": \"GPS, GLONASS, BDS, GALILEO\"}','{\"featuresOther1\": \"Samsung DeX, Samsung Wireless DeX (desktop experience support)\", \"featuresOther2\": \"Bixby natural language commands and dictation\", \"featuresOther3\": \"Samsung Pay (Visa, MasterCard certified)\", \"featuresOther4\": \"Ultra Wideband (UWB) support\"}','{\"batteryType\": \"Li-Ion 5000 mAh, non-removable\", \"batteryCharging\": \"45W wired, PD3.0\\\\n 15W wireless (Qi/PMA)\\\\n 4.5W reverse wireless\"}'),('483a2a72-b8fe-427d-9d70-69a57ba2b75a','ef39645b-212e-4a8b-b34e-1d491ad4ae62','{\"yearValue\": \"2022\", \"brandValue\": \"Samsung\", \"modelValue\": \"Galaxy S22 Ultra 5G\"}','{\"networkSpeed\": \"HSPA 42.2/5.76 Mbps, LTE-A (7CA) Cat20 2000/200 Mbps, 5G (5+ Gbps DL)\", \"network2GBands\": \"GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (Dual SIM model only)\\\\nCDMA 800 / 1900 & TD-SCDMA\", \"network3GBands\": \"HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100\\\\nCDMA2000 1xEV-DO\", \"network4GBands\": \"1, 2, 3, 4, 5, 7, 8, 12, 13, 17, 18, 19, 20, 25, 26, 28, 32, 38, 39, 40, 41, 66 - International\\\\n1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 18, 19, 20, 25, 26, 28, 29, 30, 38, 39, 40, 41, 46, 48, 66, 71 - USA\", \"network5GBands\": \"1, 2, 3, 5, 7, 8, 12, 20, 25, 28, 38, 40, 41, 66, 75, 77, 78 SA/NSA/Sub6 - International\\\\n1, 3, 5, 7, 8, 20, 28, 38, 41, 66, 71, 260, 261 SA/NSA/Sub6/mmWave - USA\", \"networkTechnology\": \"GSM / CDMA / HSPA / EVDO / LTE / 5G\"}','{\"launchStatus\": \"Available. Released 2022, February 25\", \"launchAnnounced\": \"2022, February 09\"}','{\"bodySim\": \"Nano-SIM and eSIM or Dual SIM (2 Nano-SIMs and eSIM, dual stand-by)\", \"bodyBuild\": \"Glass front (Gorilla Glass Victus+), glass back (Gorilla Glass Victus+), aluminum frame\", \"bodyOther1\": \"IP68 dust/water resistant (up to 1.5m for 30 mins)\", \"bodyOther2\": \"Armor aluminum frame with tougher drop and scratch resistance (advertised)\", \"bodyOther3\": \"Stylus, 2.8ms latency (Bluetooth integration, accelerometer, gyro)\", \"bodyWeight\": \"228 g / 229 g (mmWave) (8.04 oz)\", \"bodyDimensions\": \"163.3 x 77.9 x 8.9 mm (6.43 x 3.07 x 0.35 in)\"}','{\"displaySize\": \"6.8 inches, 114.7 cm2 (~90.2% screen-to-body ratio)\", \"displayType\": \"Dynamic AMOLED 2X, 120Hz, HDR10+, 1750 nits (peak)\", \"displayOther1\": \"Always-On display\", \"displayProtection\": \"Corning Gorilla Glass Victus+\", \"displayResolution\": \"1440 x 3088 pixels (~500 ppi density)\"}','{\"platformOs\": \"Android 12, upgradable to Android 13, One UI 5\", \"platformCpu\": \"Octa-core (1x2.8 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.8 GHz Cortex-A510) - Europe\\\\nOcta-core (1x3.00 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.80 GHz Cortex-A510) - ROW\", \"platformGpu\": \"Xclipse 920 - Europe\\\\nAdreno 730 - ROW\", \"platformChipset\": \"Exynos 2200 (4 nm) - Europe\\\\nQualcomm SM8450 Snapdragon 8 Gen 1 (4 nm) - ROW\"}','{\"memoryOther1\": \"UFS 3.1\", \"memoryCardSlot\": \"No\", \"memoryInternal\": \"128GB 8GB RAM, 256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM\"}','{\"mainCameraQuad\": \"108 MP, f/1.8, 23mm (wide), 1/1.33\\\", 0.8µm, PDAF, Laser AF, OIS\\\\n 10 MP, f/4.9, 230mm (periscope telephoto), 1/3.52\\\", 1.12µm, dual pixel PDAF, OIS, 10x optical zoom\\\\n 10 MP, f/2.4, 70mm (telephoto), 1/3.52\\\", 1.12µm, dual pixel PDAF, OIS, 3x optical zoom\\\\n 12 MP, f/2.2, 13mm, 120˚ (ultrawide), 1/2.55\\\", 1.4µm, dual pixel PDAF, Super Steady video\", \"mainCameraVideo\": \"8K@24fps, 4K@30/60fps, 1080p@30/60/240fps, 720p@960fps, HDR10+, stereo sound rec., gyro-EIS\", \"mainCameraFeatures\": \"LED flash, Auto-HDR, panorama\"}','{\"selfieCameraVideo\": \"4K@30/60fps, 1080p@30fps\", \"selfieCameraSingle\": \"40 MP, f/2.2, 26mm (wide), 1/2.82\\\", 0.7µm, PDAF\", \"selfieCameraFeatures\": \"Dual video call, Auto-HDR\"}','{\"soundOther1\": \"32-bit/384kHz audio\", \"soundOther2\": \"Tuned by AKG\", \"sound35MmJack\": \"No\", \"soundLoudspeaker\": \"Yes, with stereo speakers\"}','{\"communicationsNfc\": \"Yes\", \"communicationsUsb\": \"USB Type-C 3.2, OTG\", \"communicationsWlan\": \"Wi-Fi 802.11 a/b/g/n/ac/6e, dual-band, Wi-Fi Direct\", \"communicationsRadio\": \"No\", \"communicationsBluetooth\": \"5.2, A2DP, LE\", \"communicationsPositioning\": \"GPS, GLONASS, BDS, GALILEO\"}','{\"featuresOther1\": \"Samsung DeX, Samsung Wireless DeX (desktop experience support)\", \"featuresOther2\": \"Bixby natural language commands and dictation\", \"featuresOther3\": \"Samsung Pay (Visa, MasterCard certified)\", \"featuresOther4\": \"Ultra Wideband (UWB) support\"}','{\"batteryType\": \"Li-Ion 5000 mAh, non-removable\", \"batteryCharging\": \"45W wired, PD3.0\\\\n 15W wireless (Qi/PMA)\\\\n 4.5W reverse wireless\"}');
/*!40000 ALTER TABLE `features` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `models`
--

DROP TABLE IF EXISTS `models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `models` (
  `id` varchar(60) NOT NULL,
  `model_name` varchar(32) NOT NULL,
  `brand_id` varchar(60) NOT NULL,
  `model_img` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `model_name` (`model_name`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `models_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brands` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `models`
--

LOCK TABLES `models` WRITE;
/*!40000 ALTER TABLE `models` DISABLE KEYS */;
INSERT INTO `models` VALUES ('0653b5f6-8486-46fb-8a70-64976d513f40','Galaxy Z Fold','b7b2c51e-a5eb-40ef-9535-05da233ef5f4','https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-z-fold5-5g.jpg'),('369e37aa-d818-44be-b772-79378570d122','Galaxy Tab S8','b7b2c51e-a5eb-40ef-9535-05da233ef5f4','https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-tab-s8.jpg'),('9a695185-9eff-4ce3-9b3e-3f5735aee7c9','M34 5G','b7b2c51e-a5eb-40ef-9535-05da233ef5f4','https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m34-5g.jpg'),('ef39645b-212e-4a8b-b34e-1d491ad4ae62','Galaxy S22 5G','b7b2c51e-a5eb-40ef-9535-05da233ef5f4','https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s22-5g.jpg');
/*!40000 ALTER TABLE `models` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `secondary`
--

DROP TABLE IF EXISTS `secondary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `secondary` (
  `id` varchar(60) NOT NULL,
  `inner_key` varchar(256) DEFAULT NULL,
  `inner_value` varchar(2500) DEFAULT NULL,
  `feature_id` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `feature_id` (`feature_id`),
  CONSTRAINT `secondary_ibfk_1` FOREIGN KEY (`feature_id`) REFERENCES `features` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secondary`
--

LOCK TABLES `secondary` WRITE;
/*!40000 ALTER TABLE `secondary` DISABLE KEYS */;
INSERT INTO `secondary` VALUES ('03065a5d-a58b-4ad7-847b-70338d120604','featuresOther3','Samsung Pay (Visa, MasterCard certified)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('04503fd8-0231-45f5-9a7d-3a8c4be50ec4','network2GBands','GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (Dual SIM model only)\\nCDMA 800 / 1900 & TD-SCDMA','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('08a3ffe0-97ec-4ea4-bb38-9430a1f76e06','network5GBands','1, 2, 3, 5, 7, 8, 12, 20, 25, 28, 38, 40, 41, 66, 75, 77, 78 SA/NSA/Sub6 - International\\n1, 3, 5, 7, 8, 20, 28, 38, 41, 66, 71, 260, 261 SA/NSA/Sub6/mmWave - USA','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('1335c724-7bd2-434e-b6d5-827d66b94dce','launchAnnounced','2022, February 09','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('152d3fce-9647-4a0c-b616-a96c9bce9076','mainCameraVideo','8K@24fps, 4K@30/60fps, 1080p@30/60/240fps, 720p@960fps, HDR10+, stereo sound rec., gyro-EIS','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('1685bf3b-931a-417b-a245-7b9060d95d21','platformOs','Android 12, upgradable to Android 13, One UI 5','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('1d8f2bea-877f-4aff-aae8-2e344fc4e711','featuresOther4','Ultra Wideband (UWB) support','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('1e2fa832-55b4-47f7-baf2-e6b46ff8392a','displayProtection','Corning Gorilla Glass Victus+','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('200eb33b-175a-4ca3-bb4a-92049b7d4d94','soundLoudspeaker','Yes, with stereo speakers','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('20250de2-b0ff-4996-bf43-8d9bd94727af','featuresOther1','Samsung DeX, Samsung Wireless DeX (desktop experience support)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('22658ce2-0f0c-4d26-9f17-2e8ae3452bf8','bodyOther2','Armor aluminum frame with tougher drop and scratch resistance (advertised)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('22785cab-d035-48ea-81ee-8863d543d13c','selfieCameraFeatures','Dual video call, Auto-HDR','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('2384508a-4fa5-42ee-9219-ecd2a0d12f73','displayOther1','Always-On display','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('24d4e5b7-a279-46b5-9490-2d1a808ab234','bodyOther3','Stylus, 2.8ms latency (Bluetooth integration, accelerometer, gyro)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('28bfe2aa-f65d-495e-aef0-e8e328a5cc5b','bodyBuild','Glass front (Gorilla Glass Victus+), glass back (Gorilla Glass Victus+), aluminum frame','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('295a49d6-2c09-4243-9de8-c13fb112b2c4','selfieCameraSingle','40 MP, f/2.2, 26mm (wide), 1/2.82\", 0.7µm, PDAF','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('2b7b0956-54a2-429f-b72a-1c674f9f2eb6','launchAnnounced','2022, February 09','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('2c50e672-df37-4d13-99dd-787b672a8d75','displaySize','6.8 inches, 114.7 cm2 (~90.2% screen-to-body ratio)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('2db1eb89-0840-4ce2-bd3a-3cb8a877abb9','mainCameraFeatures','LED flash, Auto-HDR, panorama','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('2e9c5ae0-327f-4135-8915-b8778adf48aa','bodyOther2','Armor aluminum frame with tougher drop and scratch resistance (advertised)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('31342267-72fc-4895-bc31-5ace19b8a484','yearValue','2022','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('32a7152b-77ca-40d6-9a0c-ea8115888205','communicationsPositioning','GPS, GLONASS, BDS, GALILEO','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('34caae46-ad9d-4ff7-9a87-c0f3dbaceefe','bodyBuild','Glass front (Gorilla Glass Victus+), glass back (Gorilla Glass Victus+), aluminum frame','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('363d70c6-8153-4982-9f2e-214d015eaaa9','network4GBands','1, 2, 3, 4, 5, 7, 8, 12, 13, 17, 18, 19, 20, 25, 26, 28, 32, 38, 39, 40, 41, 66 - International\\n1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 18, 19, 20, 25, 26, 28, 29, 30, 38, 39, 40, 41, 46, 48, 66, 71 - USA','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('3b75bd2b-df8b-47d5-9c80-e1fde3d1a6b2','networkTechnology','GSM / CDMA / HSPA / EVDO / LTE / 5G','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('3cb49399-1149-4cc0-aaa9-fc8d4a8f7bfa','platformChipset','Exynos 2200 (4 nm) - Europe\\nQualcomm SM8450 Snapdragon 8 Gen 1 (4 nm) - ROW','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('3ccf4bc9-619e-43e6-8a87-cde1e92d62af','batteryType','Li-Ion 5000 mAh, non-removable','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('3f12f533-f478-485b-a72d-53b5a53b1b6d','communicationsNfc','Yes','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('4139d189-2424-4e88-a410-db84f2628a03','networkTechnology','GSM / CDMA / HSPA / EVDO / LTE / 5G','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('453e51a4-6987-4408-a70c-287b8258320e','mainCameraFeatures','LED flash, Auto-HDR, panorama','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('4841e7e1-a65b-4296-a52c-2551e1002b64','platformCpu','Octa-core (1x2.8 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.8 GHz Cortex-A510) - Europe\\nOcta-core (1x3.00 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.80 GHz Cortex-A510) - ROW','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('4ccc8662-112f-47fd-9920-6731effe83ca','network3GBands','HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100\\nCDMA2000 1xEV-DO','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('4e636972-0d44-478e-abbf-ae151733f2ff','memoryCardSlot','No','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('4f8e448c-e308-467e-81d8-6d8ec91f6804','brandValue','Samsung','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('503efa73-a004-46dc-baca-e0516aed139f','bodyDimensions','163.3 x 77.9 x 8.9 mm (6.43 x 3.07 x 0.35 in)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('50b88079-0939-42f1-8446-a854ae03791e','platformChipset','Exynos 2200 (4 nm) - Europe\\nQualcomm SM8450 Snapdragon 8 Gen 1 (4 nm) - ROW','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('56cfdfb6-9e5a-4a62-b3a4-41d03538e907','communicationsRadio','No','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('57e3adde-1711-4bac-bece-17652828312b','selfieCameraSingle','40 MP, f/2.2, 26mm (wide), 1/2.82\", 0.7µm, PDAF','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('5e4b9e23-1614-4023-8690-d299f7770ea2','platformGpu','Xclipse 920 - Europe\\nAdreno 730 - ROW','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('5fc34a2f-6984-435a-836e-9e2d584d33fa','selfieCameraVideo','4K@30/60fps, 1080p@30fps','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('61c2dfe1-65a5-4f9e-a605-8294cf087eb5','bodyDimensions','163.3 x 77.9 x 8.9 mm (6.43 x 3.07 x 0.35 in)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('630e7b2a-e76f-4622-9d9c-15e2e7a3ab99','launchStatus','Available. Released 2022, February 25','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('63fb1a25-8dd4-4cc7-bea6-6b534c6af146','featuresOther2','Bixby natural language commands and dictation','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('658cc15c-2260-43df-b9d1-bc640eede84c','communicationsUsb','USB Type-C 3.2, OTG','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('6a6221da-19bb-4e1c-bf57-635d3a60e7ad','featuresOther1','Samsung DeX, Samsung Wireless DeX (desktop experience support)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('76a8d20f-a7f8-4b40-9c45-8c75ec1f5ad8','network4GBands','1, 2, 3, 4, 5, 7, 8, 12, 13, 17, 18, 19, 20, 25, 26, 28, 32, 38, 39, 40, 41, 66 - International\\n1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 18, 19, 20, 25, 26, 28, 29, 30, 38, 39, 40, 41, 46, 48, 66, 71 - USA','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('788da6f7-c839-4515-b46c-8c4694b8978c','memoryOther1','UFS 3.1','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('78f47690-48c5-4eea-8246-22b780783ad3','soundOther2','Tuned by AKG','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('7ae789ec-a3cd-4bc2-b4c1-46a79e388447','selfieCameraVideo','4K@30/60fps, 1080p@30fps','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('7bb4a371-4dae-4834-b7e5-c5f0f429b74b','modelValue','Galaxy S22 Ultra 5G','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('7c122bbc-69fe-4654-b12b-dd127d9df076','networkSpeed','HSPA 42.2/5.76 Mbps, LTE-A (7CA) Cat20 2000/200 Mbps, 5G (5+ Gbps DL)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('7d73eb27-0385-45f6-9006-58b76239c8f7','communicationsWlan','Wi-Fi 802.11 a/b/g/n/ac/6e, dual-band, Wi-Fi Direct','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('7dd3e000-66b6-44ce-86a7-2cac7742ec1b','memoryCardSlot','No','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('7e6a9300-3406-4482-84cf-905afcd203af','communicationsWlan','Wi-Fi 802.11 a/b/g/n/ac/6e, dual-band, Wi-Fi Direct','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('81562587-5c9f-4e78-a9c4-2979c1238c59','brandValue','Samsung','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('825a4158-1726-4649-9bb0-6bba42128a21','bodyOther1','IP68 dust/water resistant (up to 1.5m for 30 mins)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('84957eea-92f9-4ed5-8a19-edd8c6079832','mainCameraQuad','108 MP, f/1.8, 23mm (wide), 1/1.33\", 0.8µm, PDAF, Laser AF, OIS\\n 10 MP, f/4.9, 230mm (periscope telephoto), 1/3.52\", 1.12µm, dual pixel PDAF, OIS, 10x optical zoom\\n 10 MP, f/2.4, 70mm (telephoto), 1/3.52\", 1.12µm, dual pixel PDAF, OIS, 3x optical zoom\\n 12 MP, f/2.2, 13mm, 120˚ (ultrawide), 1/2.55\", 1.4µm, dual pixel PDAF, Super Steady video','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('84dbea20-fc12-4483-8457-acb8a85a081d','bodyOther3','Stylus, 2.8ms latency (Bluetooth integration, accelerometer, gyro)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('8c506afc-3ee4-4bd5-a082-f3a5d669b221','featuresOther4','Ultra Wideband (UWB) support','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('8ce6d244-785d-4c23-bac7-1e6f6f2e5ed7','bodySim','Nano-SIM and eSIM or Dual SIM (2 Nano-SIMs and eSIM, dual stand-by)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('8f5e13a5-beea-4a57-8c63-d94ee6152c20','communicationsBluetooth','5.2, A2DP, LE','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('9255c2f9-6b33-456f-a5e3-90f4109bf0b2','featuresOther3','Samsung Pay (Visa, MasterCard certified)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('9496808d-cf1c-472d-9566-64ab7010a9b6','mainCameraQuad','108 MP, f/1.8, 23mm (wide), 1/1.33\", 0.8µm, PDAF, Laser AF, OIS\\n 10 MP, f/4.9, 230mm (periscope telephoto), 1/3.52\", 1.12µm, dual pixel PDAF, OIS, 10x optical zoom\\n 10 MP, f/2.4, 70mm (telephoto), 1/3.52\", 1.12µm, dual pixel PDAF, OIS, 3x optical zoom\\n 12 MP, f/2.2, 13mm, 120˚ (ultrawide), 1/2.55\", 1.4µm, dual pixel PDAF, Super Steady video','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('949cdfea-56a9-49b1-92a8-b069cc80fa20','displayProtection','Corning Gorilla Glass Victus+','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('94acf36b-5db6-4f9c-b3af-b03e36c9e510','displayType','Dynamic AMOLED 2X, 120Hz, HDR10+, 1750 nits (peak)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('952511da-7b08-4424-9c45-1d8edcb03ead','bodyWeight','228 g / 229 g (mmWave) (8.04 oz)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('9a4e5190-4704-4da4-a38d-79ac0f776bdb','selfieCameraFeatures','Dual video call, Auto-HDR','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('9d0c559f-1bee-455f-bd3f-2c288991fab6','displaySize','6.8 inches, 114.7 cm2 (~90.2% screen-to-body ratio)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('9e07f8d8-c85a-4a91-b57c-ba330c72801d','batteryCharging','45W wired, PD3.0\\n 15W wireless (Qi/PMA)\\n 4.5W reverse wireless','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('a4101237-3b7e-4cb3-b620-5fc1494d3ef9','featuresOther2','Bixby natural language commands and dictation','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('a5082f5f-8c20-4821-b9cc-0e45735c4b9d','network2GBands','GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (Dual SIM model only)\\nCDMA 800 / 1900 & TD-SCDMA','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('a79403a6-bd4a-443b-afb1-8af3ca1eb527','displayResolution','1440 x 3088 pixels (~500 ppi density)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('b3739569-6b53-4398-ac52-bacb81a9454c','platformOs','Android 12, upgradable to Android 13, One UI 5','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('b3c35094-e2fd-45e4-b1e6-51871f166f6b','launchStatus','Available. Released 2022, February 25','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('b51caf68-fa25-462d-9874-4dfc48d1c1c0','network3GBands','HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100\\nCDMA2000 1xEV-DO','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('b7e9c3d9-9331-4d3f-b37a-ab165f3dead5','network5GBands','1, 2, 3, 5, 7, 8, 12, 20, 25, 28, 38, 40, 41, 66, 75, 77, 78 SA/NSA/Sub6 - International\\n1, 3, 5, 7, 8, 20, 28, 38, 41, 66, 71, 260, 261 SA/NSA/Sub6/mmWave - USA','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('b8a949ac-cecb-4495-8642-c436f62ecc70','sound35MmJack','No','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('bd60e447-189e-4dd8-aa79-e41856d31967','bodyWeight','228 g / 229 g (mmWave) (8.04 oz)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('bdc1c7ee-5736-407b-b22a-e2b7e6d38497','memoryInternal','128GB 8GB RAM, 256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('be19c0b0-0ba7-46ae-a06e-0f7039f95fd0','bodyOther1','IP68 dust/water resistant (up to 1.5m for 30 mins)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('c108a9fa-ac8a-4f4a-b7c4-dab6e9817be7','yearValue','2022','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('c1501c53-71f5-45af-8259-b9213075c575','modelValue','Galaxy Z Fold','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('c1bddfd3-dd2d-4652-95a9-793bbc03dbb3','communicationsUsb','USB Type-C 3.2, OTG','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('c28232f4-5369-4197-9370-c6308835b788','communicationsBluetooth','5.2, A2DP, LE','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('c8bebc02-71d9-461b-a868-c7163be384d7','soundOther1','32-bit/384kHz audio','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('c90d32dc-afaf-4040-b3fe-23e3ee450dcd','communicationsPositioning','GPS, GLONASS, BDS, GALILEO','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('cafb2adc-8d1c-492e-b991-fcd5f46de844','platformGpu','Xclipse 920 - Europe\\nAdreno 730 - ROW','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('ce8e9b6b-e6f0-41c0-b967-21f4a8641cd8','displayType','Dynamic AMOLED 2X, 120Hz, HDR10+, 1750 nits (peak)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('cfdebf91-e01a-4dec-a185-bc172a6d29bb','memoryInternal','128GB 8GB RAM, 256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('d16171fa-7748-4f53-9f87-4dd56c1a6544','communicationsRadio','No','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('d2908fb3-49b0-4af3-b135-4482de80918d','sound35MmJack','No','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('db269f2f-8843-4b31-817d-0e66b6ea41dd','soundOther2','Tuned by AKG','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('ddb8d5bb-f62a-43c6-810e-f152fe71a81d','soundOther1','32-bit/384kHz audio','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('e24f69f0-8467-473d-b5f9-080477da2a42','batteryType','Li-Ion 5000 mAh, non-removable','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('e3ba9e3c-4972-4d66-b77b-9bf907a3d1fc','platformCpu','Octa-core (1x2.8 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.8 GHz Cortex-A510) - Europe\\nOcta-core (1x3.00 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.80 GHz Cortex-A510) - ROW','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('e4be730c-ef3b-48ac-9cfc-5b605d504e38','memoryOther1','UFS 3.1','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('e8aec697-c8b8-4b11-a197-e102ae331d2f','displayResolution','1440 x 3088 pixels (~500 ppi density)','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('ec3ae468-9855-457c-a138-6cf7b56cf829','batteryCharging','45W wired, PD3.0\\n 15W wireless (Qi/PMA)\\n 4.5W reverse wireless','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('ee25430d-8cbf-4437-b026-e9641a46076b','displayOther1','Always-On display','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('eee53b38-2107-414b-9072-763d204f9b0d','networkSpeed','HSPA 42.2/5.76 Mbps, LTE-A (7CA) Cat20 2000/200 Mbps, 5G (5+ Gbps DL)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('ef90e4d0-69b1-430f-ab12-4be404b80a7a','communicationsNfc','Yes','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('f4dab826-a0a4-4d98-97a4-546fc1def57a','bodySim','Nano-SIM and eSIM or Dual SIM (2 Nano-SIMs and eSIM, dual stand-by)','483a2a72-b8fe-427d-9d70-69a57ba2b75a'),('f70fa554-bc81-4bb5-a1b0-d1ce47cee3c8','soundLoudspeaker','Yes, with stereo speakers','383e8d93-9017-40d7-bd1a-ab9e6878539e'),('fe5a7270-a704-40c3-bf33-a989e0baa03b','mainCameraVideo','8K@24fps, 4K@30/60fps, 1080p@30/60/240fps, 720p@960fps, HDR10+, stereo sound rec., gyro-EIS','483a2a72-b8fe-427d-9d70-69a57ba2b75a');
/*!40000 ALTER TABLE `secondary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `summaries`
--

DROP TABLE IF EXISTS `summaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `summaries` (
  `id` varchar(60) NOT NULL,
  `model_id` varchar(60) NOT NULL,
  `Release` varchar(32) DEFAULT NULL,
  `Screen` varchar(32) DEFAULT NULL,
  `Memory` varchar(32) DEFAULT NULL,
  `Storage` varchar(32) DEFAULT NULL,
  `Camera` varchar(32) DEFAULT NULL,
  `Battery` varchar(32) DEFAULT NULL,
  `Gaming` varchar(32) DEFAULT NULL,
  `Photography` varchar(32) DEFAULT NULL,
  `SocialMedia` varchar(32) DEFAULT NULL,
  `Publishing` varchar(32) DEFAULT NULL,
  `Marketting` varchar(32) DEFAULT NULL,
  `Multimedia` varchar(32) DEFAULT NULL,
  `Basic` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `model_id` (`model_id`),
  CONSTRAINT `summaries_ibfk_1` FOREIGN KEY (`model_id`) REFERENCES `models` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `summaries`
--

LOCK TABLES `summaries` WRITE;
/*!40000 ALTER TABLE `summaries` DISABLE KEYS */;
INSERT INTO `summaries` VALUES ('8514b309-ff06-4e88-8ede-9e23af988e62','9a695185-9eff-4ce3-9b3e-3f5735aee7c9','September 9, 2018','6.5 inches','4GB','32GB','16MP','4000mAh','LowEnd','Medium','Optimal','Good',NULL,'Optimal','Optimal'),('87e3a485-3191-4891-8734-18c19e0915a1','ef39645b-212e-4a8b-b34e-1d491ad4ae62','February 25, 2022','6.1 inches','8GB RAM','128/256GB Built-in','50MP(Rear)','3700 mAh','HighEnd','High',NULL,'Optimal','Optimal','Optimal','Optimal'),('d7202d75-0d8c-4f2a-ac1f-7ef86552eec7','0653b5f6-8486-46fb-8a70-64976d513f40','September 12, 2018','6.5 inches','4GB RAM','64/256/512 Built-in','50MP(Rear)','3100 mAh','HighEnd','High',NULL,'Optimal','Optimal','Optimal','Optimal');
/*!40000 ALTER TABLE `summaries` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-17  9:46:35
